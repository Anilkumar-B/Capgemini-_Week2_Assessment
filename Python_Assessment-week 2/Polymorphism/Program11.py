"""•	11. Create a class `Logger` with a method `log(message)`. 
Implement method overloading to log different message types (`error`, `warning`, `info`)."""

class Logger:
    def log(self,message,level='info'):
        if level=='error':
            print(f"[ERROR] {message}")
        elif level=='warning':
            print(f"[WARNING] {message}")
        elif level=='info':
            print(f"[INFO] {message}")
        else:
            print(f"[UNKNOWN] {message}")

logger=Logger()
print(f"This is error","error")
print(f"This is warning","warning")
print(f"This is info","info")
print(f"Unknown message","unknown")