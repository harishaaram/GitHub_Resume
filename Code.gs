// Collects the Unread message from Inbox and stores it in the spreadsheet

var SHEET_ID = '1N8BAv74hpnld2Cj3AA9jiyl6W5YN9-abDUiYi0RJbp0';

function myFunction() {
  
  var ss = SpreadsheetApp.openById(SHEET_ID);

  var threads = GmailApp.search('label:Inbox is:unread', 0, 5);
  for (var i=0; i<threads.length; i++)
  {
    var messages = threads[i].getMessages();

    for (var j=0; j<messages.length; j++)
    {
      var from = messages[j].getFrom();
      var sub = messages[j].getSubject();
      var dat = messages[j].getDate();
//      var bod = messages[j].getPlainBody();

      ss.appendRow([sub, dat, from])
    }
  }
}
