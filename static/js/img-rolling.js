function rollingInit(wrapName)
{
    // --------图片轮播
    var btnl = $(wrapName + " .rollingl"),
        btnr = $(wrapName + " .rollingr"),
        imgs = $(wrapName + " ul li"),
        wrap = $(wrapName);
    var i = 0,
        len = imgs.length-1,
        isInit = false;

    function toggle()
    {
        imgs.eq(i).fadeIn(700).siblings().hide();        
    }

    var roll2l = function()
    {
        if(i == 0)
        {
            i = len + 1;
        }

        i--;
        toggle();
    }
    var roll2r = function()
    {
        if(i == len)
        {
            i = -1;
        }

        i++;
        toggle();
    };

    imgs.eq(0).show();

    if(len == 0)
    {
        btnl.hide();
        btnr.hide();
    }
    else
    {
        btnl.click(roll2l);
        btnr.click(roll2r);

        // 设置自动轮播
        var time = setInterval(roll2r, 3000);
        wrap.hover(function()
        {
            clearInterval(time);
            time = setInterval(roll2r,5000);
        }
        ,function()
        {
            clearInterval(time);
            time = setInterval(roll2r,3000);
        });
    }

    // --------图片轮播 end ---
}