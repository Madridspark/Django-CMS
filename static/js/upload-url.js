$(function()
{
    $("article img").each(function()
    {
        var rsc = $(this).attr("src")
        if(rsc.match("/static/upload/") == null)
        {
            $(this).attr("src", "/static/upload/" + rsc)
        }
    });
    
});