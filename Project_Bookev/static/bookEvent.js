    $(document).ready(function (){
       if(!sessionStorage.getItem('email'))
        {
            alert("You need to login to access this page.");
            window.location.href='/';
        }
               $("#submit").on('click', function(){

            var formdata = $("#book").serializeArray();
            var data = {};
            flag = false;
       var yr,mon,dateDay,stHr,endHr,stMin,endMin;
            $(formdata ).each(function(index, obj){
                if(obj.value=="")
           {
               flag = true;
           }
           if(obj.name=="date")
           {
               yr = parseInt(obj.value.slice(0,4));
               mon = parseInt(obj.value.slice(5,7));
               dateDay = parseInt(obj.value.slice(8,10));
           }
           if(obj.name == "startTime")
           {
               stHr = parseInt(obj.value.slice(0,2));
               stMin = parseInt(obj.value.slice(3,5));
           }
           if(obj.name == "endTime")
           {
               endHr = parseInt(obj.value.slice(0,2));
               endMin = parseInt(obj.value.slice(3,5));
           }
                data[obj.name] = obj.value;
            });
            if(flag)
       {alert("All fields must be filled.");
           return;}

       if(stHr > endHr)
       {
           alert("Start time cannot be greater than end time.");
           return;
       }
       else if(stHr == endHr)
       {
           if(stMin > endMin)
           {
               alert("Start time cannot be greater than end time.");
           return;
           }
               else if(stMin==endMin)
           {
               alert("Start time and end time cannot be equal.");
           return;
           }
       }

       const date = new Date();

        let day = date.getDate();
        let month = date.getMonth() + 1;
        let year = date.getFullYear();

        if(yr < year)
        {
            alert("The date has already passed.");
            return;
        }
        else if(yr == year)
        {
            if(mon < month)
            {
                alert("The date has already passed.");
            return;
            }
            else if(mon == month)
            {
                if(dateDay < day)
                {
                    alert("The date has already passed.");
            return;
                }
                else if(dateDay == day)
                {
                    alert("Can't book for today. We need one day advance information.");
                    return;
                }

            }
        }
            data['userMail'] = sessionStorage.getItem('email');
            data=JSON.stringify(data)
            $.ajax({
                url: '/api/fullevent',
                type : "POST",
                data : data,
                dataType : 'json',
                contentType: "application/json; charset=utf-8",

                success : function(result) {
                    alert("Event booked successfully!\nOur team will get in touch with you soon.");
                    window.location.href='/';
                },
                error: function(xhr, resp, text) {
                    console.log(xhr, resp, text);
                }
            })

    });
    });