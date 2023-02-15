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
            $("#hireDesigner").on('click',function(){
       var formdata = $("#book").serializeArray();
       data = {};
       flag = false;
       var yr,mon,dateDay;
       $(formdata).slice(0,1).each(function (index,obj){
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
              email = sessionStorage.getItem('toBookEmail');
              var count = 0;
              if(response.length != 0)
              {
                  $(response).each(function (index,obj){

                     if(obj.serviceMail == email)
                     {
                         yr = parseInt(obj.date.slice(0,4))
                         mon = parseInt(obj.date.slice(5,7))
                         dateDay = parseInt(obj.date.slice(8,10))
                         if(yr > year)
                         {
                             count = count + 1;
                         }
                         else if(year == yr)
                         {
                             if(mon > month)
                             {
                                 count = count + 1;
                             }
                             else if(mon == month)
                             {
                                 if(dateDay > day)
                                     count = count + 1;
                             }
                         }
                     }
                  });
              }

              if(count < sessionStorage.getItem('maxLimit')) {
                  data['startTime'] = "";
                  data['endTime'] = "";
                  data['userMail'] = sessionStorage.getItem('email');
                  data['serviceMail'] = sessionStorage.getItem('toBookEmail');
                  var charges = sessionStorage.getItem('chargesPerDress')
                  var noOfDresses = formdata[1].value;
                  data['charges'] = charges * noOfDresses;
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
