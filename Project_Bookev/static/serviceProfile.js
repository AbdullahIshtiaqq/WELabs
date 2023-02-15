
        $(document.body).ready(function (e) {
            if(!sessionStorage.getItem('email') || sessionStorage.getItem('type') != 'service')
        {
            alert("You need to login as service provider to access this page.");
            window.location.href='/';
        }
             $("#logout").on('click',function(){
           sessionStorage.clear();
           window.location.href='/';
        });
            $("#name").text(sessionStorage.getItem('loginName'));
            $("#email").text(sessionStorage.getItem('email'));
            $("#mobile").text(sessionStorage.getItem('mobile'));
                 $.ajax({type:"GET",
                     url:"/api/review",
                     success: function(result){
                         myData3 = []
                         $(result).each(function (index,obj){
                            if(obj.serviceMail == sessionStorage.getItem('email'))
                            {
                                myData3.push(obj);
                            }
                         });
                         if(myData3 !=null || myData3 !=""){
                            table = $('#show3').DataTable( {
                                data: myData3 ,destroy: true,
                                columns: [
                                    { data: 'userMail' },
                                    { data: 'feedback' },




                                ]
                            } );
                        }

                  }});

                 $.ajax({type:"GET",
                     url:"/api/booking",
                     success: function(result){

                         myData1 = []
                         myData2 = []
                         const date = new Date();

                        let day = date.getDate();
                        let month = date.getMonth() + 1;
                        let year = date.getFullYear();
                         $(result).each(function (index,obj){
                            if(obj.serviceMail == sessionStorage.getItem('email'))
                            {
                                var yr,mon,dateDay;
                                yr = parseInt(obj.date.slice(0,4));
                               mon = parseInt(obj.date.slice(5,7));
                               dateDay = parseInt(obj.date.slice(8,10));

                               if(yr < year)
                                {
                                    myData1.push(obj);
                                }
                                else if(yr == year)
                                {
                                    if(mon < month)
                                    {
                                        myData1.push(obj);
                                    }
                                    else if(mon == month)
                                    {
                                        if(dateDay < day)
                                        {
                                           myData1.push(obj);
                                        }
                                        else {
                                            myData2.push(obj);
                                        }

                                    }
                                    else
                                        myData2.push(obj);
                                }
                                else myData2.push(obj);
                            }
                         });
                            table = $('#show1').DataTable( {
                                data: myData1 ,destroy: true,
                                columns: [
                                    { data: 'userMail' },
                                    { data: 'date' },
                                    { data: 'charges' },




                                ]
                            } );
                            table = $('#show2').DataTable( {
                                data: myData2 ,destroy: true,
                                columns: [
                                    { data: 'userMail' },
                                    { data: 'date' },
                                    { data: 'charges' },




                                ]
                            } );
                        }

                  });
        });