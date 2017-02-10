$(function()
{
    rollingInit("#hero");

    $(window).resize(function()
    {
        var windowWidth = $(window).width();

        if(windowWidth < 1180)
        {
            windowWidth = 1180;
        }

        $("html").css("width", windowWidth);
    });

    $(".list-content").each(function()
    {
        $(this).html("<p>" +$(this).text() + "</p>");

        var $p = $("p", $(this)).eq(0);

        ellipsis($p, 2, 17, 6);
    });
});

function ellipsis($p, lineHeight, fontSize, lines)
{
    while ($p.outerHeight() > lineHeight*fontSize*lines)
    {
        $p.text($p.text().replace(/(\s)*([a-zA-Z0-9]+|\W)(\.\.\.)?$/, "..."));
    };

    $p.css("min-height", lineHeight*fontSize*lines);
}