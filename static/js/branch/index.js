$(function()
{
    var textList = $("#hot-text li"),
        className = "hot-current";

    textList.eq(0).addClass(className);

    var toggleText = function(index)
    {
        textList.removeClass(className);
        textList.eq(index).addClass(className);
    }

    var imageRolling = rollingInit("#hot-img", toggleText);

    textList.hover(function()
    {
        imageRolling.toggleImage(textList.index($(this)));
        imageRolling.clearInt();
    },
    function()
    {
        imageRolling.setInt();
    });
});