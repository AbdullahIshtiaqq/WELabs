$(document).ready(function (){
            if(sessionStorage.getItem('email'))
            {
                $("#withoutLogin").hide();
            }
            else {
                $("#withLogin").hide();
            }
            $("#logout").on('click',function(){
                sessionStorage.clear();
                window.location.href='/';
            });
    });

window.onload=function() {
    let myDiv1 = document.getElementById("part1");
    myDiv1.addEventListener("click", function () {
        window.location.href = "/bookev/photography";
    });

    let myDiv2 = document.getElementById("part2");
    myDiv2.addEventListener("click", function () {
        window.location.href = "/bookev/catering";
    });

    let myDiv3 = document.getElementById("part3");
    myDiv3.addEventListener("click", function () {
        window.location.href = "/bookev/designing";
    });

    let myDiv4 = document.getElementById("part4");
    myDiv4.addEventListener("click", function () {
        window.location.href = "/bookev/decoration";
    });

    let myDiv5 = document.getElementById("part5");
    myDiv5.addEventListener("click", function () {
        window.location.href = "/bookev/venue";
    });

    let myDiv = document.getElementById("part6");
    myDiv.addEventListener("click", function () {
        window.location.href = "/bookev/events";
    });
}