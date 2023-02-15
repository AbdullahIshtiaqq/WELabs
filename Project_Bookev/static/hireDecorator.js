    $(document).ready(function(){
        if(!sessionStorage.getItem('email'))
        {
            alert("You need to login to access this page.");
            window.location.href='/';
        }
        $.ajax({type:"GET",
                     url:"/api/review",
                     success: function(result){
                         myData = []
                         $(result).each(function (index,obj){
                            if(obj.serviceMail == sessionStorage.getItem('toBookEmail'))
                            {
                                myData.push(obj);
                            }
                         });
                         if(myData !=null || myData !=""){
                            table = $('#show').DataTable( {
                                data: myData ,destroy: true,
                                columns: [
                                    { data: 'userMail' },
                                    { data: 'feedback' },




                                ]
                            } );
                        }

                  }});
            $("#bookSubmit").on('click',function(){
       var formdata = $("#book").serializeArray();
       data = {};
       flag = false;
       var yr,mon,dateDay,stHr,endHr,stMin,endMin;
       $(formdata).slice(0,2).each(function (index,obj){
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

       $.ajax({
          url: '/api/booking',
          type: 'get',
          success:function (response){
              var post = true;
              email = sessionStorage.getItem('toBookEmail');
              if(response.length != 0)
              {
                  $(response).each(function (index,obj){
                     if(obj.serviceMail == email)
                     {
                         if(obj.date == data['date'])
                         {
                             var startHour = parseInt(obj.startTime.slice(0,2));
                             var endHour = parseInt(obj.endTime.slice(0,2));
                             stHr = endHr - formdata[2].value;
                             if((startHour>= stHr && startHour <= endHr) || (endHour>= stHr && endHour <= endHr))
                             {
                                 post = false;
                             }

                         }
                     }
                  });
              }

              if(post) {
                  data['startTime'] =(endHr - formdata[2].value).toString()+':'+endMin.toString();
                  data['userMail'] = sessionStorage.getItem('email');
                  data['serviceMail'] = sessionStorage.getItem('toBookEmail');
                  var charges = sessionStorage.getItem('chargesPerHour')
                  data['charges'] = charges * formdata[2].value;
                  data = JSON.stringify(data);
                  $.ajax({
                      url: '/api/booking',
                      type: 'post',
                      data: data,
                      dataType: 'json',
                      contentType: "application/json; charset=utf-8",
                      success: function (response) {
                          msg = 'Booking Confirmed!\nYou can contact ' + sessionStorage.getItem('name') + ' at:\n';
                          msg = msg + 'Email: ' + sessionStorage.getItem('toBookEmail') + '\nMobile No. ' + sessionStorage.getItem('mobileNo');
                          alert(msg);
                          window.location.href = '/';
                      }
                  });
              }
              else
                  alert("This service provider has already booking at this time!");
          }
       });
    });
    });