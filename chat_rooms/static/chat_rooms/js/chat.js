$(document).ready(function()
{
    $("#chat_messages").scrollTop($("#chat_messages")[0].scrollHeight);
    
    function refresh()
    {
        var div = $('#chat_messages'),
            divHtml = div.html();

        div.html(divHtml);

        $("#chat_messages").scrollTop($("#chat_messages")[0].scrollHeight);
    }

    setInterval(function()
    {
        refresh()
    }, 5000); // 5 secs
})