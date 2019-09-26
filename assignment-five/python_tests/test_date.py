import pytest
import main

def test_date():
   canSubmit = main.getCanSubmit()
   currentDate = "2019-10-26"
   closeDate = main.getCloseDate()
   assert canSubmit == (currentDate <= closeDate)

def test_dateFail():
    canSubmit = main.getCanSubmitFail()
    newCurrentDate = "2019-10-29"
    closeDate = main.getCloseDate()
    assert canSubmit == (newCurrentDate <= closeDate)