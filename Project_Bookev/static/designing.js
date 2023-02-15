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

    $("#hireDesigner").on('click',function (){
       var formdata = $("#id").val();
       if(formdata=="")
       {
           alert("Please enter id.");
           return;
       }
       $.ajax({
          url:'/api/designer/'+formdata,
          type: 'GET',
          success : function (response){
              if(response.email == 'Not found')
              {
                  alert("ID does not exist, please enter valid id from table.");
              }
              else
              {
                  sessionStorage.setItem('toBookEmail',response.email);
                  sessionStorage.setItem('chargesPerDress',response.charges);
                  sessionStorage.setItem('mobileNo',response.mobileNo);
                  sessionStorage.setItem('name',response.name);
                  sessionStorage.setItem('maxLimit',response.maxLimit);
                  window.location.href='/bookev/hire/designer';
              }

          }
       });
    });
        var myData
        $(document.body).ready(function (e) {
           //doStuff
            if(sessionStorage.getItem("email")) {
                $.ajax({
                    type: "GET",
                    url: "/api/designer",
                    success: function (result) {
                        myData = result
                        if (myData != null || myData != "") {
                            table = $('#show').DataTable({
                                data: myData, destroy: true,
                                columns: [
                                    {data: '_id.$oid'},
                                    {data: 'name'},
                                    {data: 'experience'},
                                    {data: 'speciality'},
                                    {data: 'charges'},


                                ]
                            });
                        }

                    }
                });
                $("#show").show();
                $("#inputField").show();
                $("#para").hide();
            }
            else
            {
                $("#show").hide();
                $("#inputField").hide();
                $("#para").show();
            }
        });


const carousel = document.querySelector(".carousel"),
firstImg = carousel.querySelectorAll("img")[0],
arrowIcons = document.querySelectorAll(".wrapper i");

let isDragStart = false, isDragging = false, prevPageX, prevScrollLeft, positionDiff;

const showHideIcons = () => {
    // showing and hiding prev/next icon according to carousel scroll left value
    let scrollWidth = carousel.scrollWidth - carousel.clientWidth; // getting max scrollable width
    arrowIcons[0].style.display = carousel.scrollLeft == 0 ? "none" : "block";
    arrowIcons[1].style.display = carousel.scrollLeft == scrollWidth ? "none" : "block";
}

arrowIcons.forEach(icon => {
    icon.addEventListener("click", () => {
        let firstImgWidth = firstImg.clientWidth + 14; // getting first img width & adding 14 margin value
        // if clicked icon is left, reduce width value from the carousel scroll left else add to it
        carousel.scrollLeft += icon.id == "left" ? -firstImgWidth : firstImgWidth;
        setTimeout(() => showHideIcons(), 60); // calling showHideIcons after 60ms
    });
});

const autoSlide = () => {
    // if there is no image left to scroll then return from here
    if(carousel.scrollLeft - (carousel.scrollWidth - carousel.clientWidth) > -1 || carousel.scrollLeft <= 0) return;

    positionDiff = Math.abs(positionDiff); // making positionDiff value to positive
    let firstImgWidth = firstImg.clientWidth + 14;
    // getting difference value that needs to add or reduce from carousel left to take middle img center
    let valDifference = firstImgWidth - positionDiff;

    if(carousel.scrollLeft > prevScrollLeft) { // if user is scrolling to the right
        return carousel.scrollLeft += positionDiff > firstImgWidth / 3 ? valDifference : -positionDiff;
    }
    // if user is scrolling to the left
    carousel.scrollLeft -= positionDiff > firstImgWidth / 3 ? valDifference : -positionDiff;
}

const dragStart = (e) => {
    // updatating global variables value on mouse down event
    isDragStart = true;
    prevPageX = e.pageX || e.touches[0].pageX;
    prevScrollLeft = carousel.scrollLeft;
}

const dragging = (e) => {
    // scrolling images/carousel to left according to mouse pointer
    if(!isDragStart) return;
    e.preventDefault();
    isDragging = true;
    carousel.classList.add("dragging");
    positionDiff = (e.pageX || e.touches[0].pageX) - prevPageX;
    carousel.scrollLeft = prevScrollLeft - positionDiff;
    showHideIcons();
}

const dragStop = () => {
    isDragStart = false;
    carousel.classList.remove("dragging");

    if(!isDragging) return;
    isDragging = false;
    autoSlide();
}

carousel.addEventListener("mousedown", dragStart);
carousel.addEventListener("touchstart", dragStart);

document.addEventListener("mousemove", dragging);
carousel.addEventListener("touchmove", dragging);

document.addEventListener("mouseup", dragStop);
carousel.addEventListener("touchend", dragStop);