$(function()
{
    isToggle = false;
    $(window).scroll(function()
    {
        if(($(window).scrollTop() > 300 && !isToggle) || ($(window).scrollTop() < 300 && isToggle))
        {
            $("#nav-bar").toggleClass("fixed");
            isToggle = !isToggle;            
        }
    });
});