"""
icm_mcp_server.py
"""

from mcp.server.fastmcp import FastMCP
from icm_controller_final2 import ICMController, ICMControllerError

mcp = FastMCP("Musa_ICM_Bridge")
controller = ICMController()


@mcp.tool()
def icm_run_ruby(ruby_code: str) -> str:
    """Run arbitrary Ruby code inside InfoWorks ICM."""
    try:
        return controller.run_ruby(ruby_code)
    except ICMControllerError as e:
        return f"ERROR: {e}"


@mcp.tool()
def icm_network_summary() -> str:
    """
    Return a summary of the currently opened InfoWorks network.
    """

    ruby = r'''
net = WSApplication.current_network

puts "Network: #{net.model_object.name}"

tables = {
  "Nodes"     => "_nodes",
  "Links"     => "_links",
  "Conduits"  => "_conduits",
  "Culverts"  => "_culverts",
  "Pumps"     => "_pumps",
  "Weirs"     => "_weirs",
  "Orifices"  => "_orifices"
}

tables.each do |name, table|
  begin
    puts "#{name}: #{net.row_objects(table).length}"
  rescue
  end
end
'''

    try:
        return controller.run_ruby(ruby)
    except ICMControllerError as e:
        return f"ERROR: {e}"


if __name__ == "__main__":
    mcp.run(transport="stdio")