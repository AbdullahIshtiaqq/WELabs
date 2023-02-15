
        $(document.body).ready(function (e) {
            if(sessionStorage.getItem('type') != 'admin')
        {
            alert("You have no permission to access this page.");
            window.location.href='/';
        }
             $("#logout").on('click',function(){
           sessionStorage.clear();
           window.location.href='/';
        });
                 $.ajax({type:"GET",
                     url:"/api/fullevent",
                     success: function(result){
                         myData = result;
                         if(myData !=null || myData !=""){
                            table = $('#show').DataTable( {
                                data: myData ,destroy: true,
                                columns: [
                                    { data: 'userMail' },
                                    { data: 'date' },
                                    { data: 'startTime'},
                                    { data: 'endTime'},
                                    { data: 'description'}




                                ]
                            } );
                        }

                  }});


        });