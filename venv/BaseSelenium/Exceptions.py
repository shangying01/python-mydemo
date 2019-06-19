import selenium.common.exceptions

def getExceptions():
    try:
        a=1
    except selenium.common.exceptions.ElementClickInterceptedExceptionn:
        print("aa")
        raise
    except selenium.common.exceptions.ElementNotInteractableException:
        print("")
        raise
    except selenium.common.exceptions.ElementNotInteractableException:
        print("")
        raise