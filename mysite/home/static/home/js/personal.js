// Open and close Main Menu on Header
$(function() {
    $('#navOpen').click(function() {
        $(this).toggleClass('active');
        compare();
    });
});

$(function() {
    $('.closebtn').click(function() {
        $('#navOpen').removeClass('active');
        compare();
    });
});

function compare() {
    if ($('#navOpen').hasClass('active')){
        $('#mainNav').css('width','100%');
    } else {
        $('#mainNav').css('width','0');
    }
};

// Mean Menu Scroll Function
var scrollTimer = null;

$(window).scroll(function() {
    var width=$(window).width()
    if(width >= 790) {
        var top = $(document).scrollTop();
        clearTimeout(scrollTimer);
        scrollTimer = setTimeout(
        function() 
        {
            if(top <= 50 && width >=790) 
            {
                $(".sidenav").css({'left':'130px','text-align':'left'});
                $(".sidenav a").css({'margin-left':'10px'});
            }
            else
            {
                $(".sidenav").css({'left':'0px','text-align':'center'});
            }
        }, 100);
    };
});
    
