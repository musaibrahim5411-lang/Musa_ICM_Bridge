import os
import time
from pywinauto import Desktop

MAIN_WINDOW_TITLE_RE = r"InfoWorks ICM \[.*\].*"
BRIDGE_FOLDER = r"C:\icm_mcp_poc"
RESULT_FILE = os.path.join(BRIDGE_FOLDER, "result.txt")


class ICMControllerError(Exception):
    pass


class ICMController:
    def __init__(self, run_timeout=30, poll_interval=0.3):
        self.run_timeout = run_timeout
        self.poll_interval = poll_interval
        os.makedirs(BRIDGE_FOLDER, exist_ok=True)

    def _get_main_window(self):
        candidates = Desktop(backend="win32").windows(title_re=MAIN_WINDOW_TITLE_RE)
        if not candidates:
            raise ICMControllerError("مش لاقي أي نافذة InfoWorks ICM شغالة.")
        for w in candidates:
            try:
                run_buttons = [b for b in w.descendants(class_name="Button") if b.window_text() == "Run"]
                if run_buttons:
                    return w, run_buttons[0]
            except Exception:
                continue
        raise ICMControllerError(
            "مش لاقي زرار 'Run'. اتأكد إن نافذة Ruby Script مفتوحة على الشاشة."
        )

    def _find_edit_near(self, run_btn):
        parent = run_btn.parent()
        edits = parent.descendants(class_name="Edit")
        if not edits:
            edits = parent.parent().descendants(class_name="Edit")
        if not edits:
            raise ICMControllerError("لقيت زرار Run بس مش لاقي الـ text editor جنبه.")
        return edits[0]

    def _type_code(self, editor, code: str):
        editor.set_focus()
        editor.type_keys("^a{DELETE}", pause=0.02)
        text_crlf = code.replace("\r\n", "\n").replace("\n", "\r\n")
        editor.set_edit_text(text_crlf)

    def _wrap_code(self, user_code: str) -> str:
        result_path_ruby = RESULT_FILE.replace("\\", "/")
        return (
            "require 'stringio'\n"
            "$__capture = StringIO.new\n"
            "$stdout = $__capture\n"
            "begin\n"
            f"{user_code}\n"
            "rescue => e\n"
            "  $__capture.puts \"ERROR: #{e.class}: #{e.message}\"\n"
            "end\n"
            "$stdout = STDOUT\n"
            f"File.open('{result_path_ruby}', 'w') {{ |f| f.write($__capture.string) }}\n"
        )

    def run_ruby(self, user_code: str, timeout: int = None) -> str:
        timeout = timeout or self.run_timeout

        if os.path.exists(RESULT_FILE):
            os.remove(RESULT_FILE)

        main_win, run_btn = self._get_main_window()
        editor = self._find_edit_near(run_btn)

        full_code = self._wrap_code(user_code)
        self._type_code(editor, full_code)
        run_btn.click()

        return self._wait_for_result_file(timeout)

    def _wait_for_result_file(self, timeout: int) -> str:
        deadline = time.time() + timeout
        while time.time() < deadline:
            if os.path.exists(RESULT_FILE):
                time.sleep(0.3)
                try:
                    with open(RESULT_FILE, "r", encoding="utf-8", errors="replace") as f:
                        content = f.read()
                    os.remove(RESULT_FILE)
                    return content
                except (PermissionError, FileNotFoundError):
                    time.sleep(0.2)
                    continue
            time.sleep(self.poll_interval)

        raise ICMControllerError(
            f"استنينا {timeout} ثانية ومفيش ملف نتيجة ظهر. "
            "ممكن السكريبت لسه شغال أو حصل خطأ منع كتابة الملف."
        )


if __name__ == "__main__":
    controller = ICMController()
    test_code = 'puts "hello from python"\nputs WSApplication.ui?'
    print("Running test code in ICM...")
    result = controller.run_ruby(test_code)
    print("=== Result ===")
    print(result)