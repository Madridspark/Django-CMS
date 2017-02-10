function rollingInit(wrapName, callBack = null)
{
    // --------图片轮播
    var btnl = $(wrapName + " .rollingl"),
        btnr = $(wrapName + " .rollingr"),
        imgs = $(wrapName + " ul li"),
        wrap = $(wrapName);
    var i = 0,
        len = imgs.length-1,
        isInit = false,
        time = 3000;

    function toggleImage(index)
    {
        i = index;
        imgs.eq(i).fadeIn(700).siblings().hide();

        if(callBack != null && callBack != undefined)
        {
            callBack(index);
        }
    }

    var roll2l = function()
    {
        if(i == 0)
        {
            i = len + 1;
        }

        i--;
        toggleImage(i);
    }
    var roll2r = function()
    {
        if(i == len)
        {
            i = -1;
        }

        i++;
        toggleImage(i);
    };

    var theTimer = 0;

    var setInt = function()
    {
        theTimer = setInterval(roll2r, time);
    }

    var clearInt = function()
    {
        clearInterval(theTimer);
    }

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
        setInt();
        wrap.hover(function()
        {
            clearInt();
        }
        ,function()
        {
            setInt();
        });
    }


    // --------图片轮播 end ---

    return (
    {
        index : i,
        toggleImage : toggleImage,
        setInt : setInt,
        clearInt : clearInt
    });
}