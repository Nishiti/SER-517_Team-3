
var brandController = app.controller("brandController", function ($scope, $window, $http, $location) {


    //console.log($window.localStorage.nxtlabUser)


    $scope.login = function checkIfLoginActive(){

        //console.log($window.localStorage.nxtlabUser);
        console.log($window.localStorage.needlogin);
        //if($location.path() ==/)
        var currentpath = $location.path();
        if (currentpath == "/brand" || currentpath == "/home") {

        }else{
            if ($window.localStorage.needlogin == "true") {
                $location.path("/login")
            }
        }

    };

    $scope.login();


    $scope.brandsignup = function() {
        console.log($scope.socialhandles);
        var data =
            {
                "company_name" : $scope.cname,
                "email" : $scope.email,
                "password" : $scope.password,
                "confirm_password" : $scope.confirm_password,
                "address" : $scope.address          
            }

        if(data.password.length < 6 || data.confirm_password.length < 6){
            alert("password is too small, please set new password with least length of 6");
        }else if(data.password != data.confirm_password){
            alert("password and confirm password is not matching");
        }else{
            $http.post('http://localhost:5000/brand', data).then(function (response) {

                console.log(response.data);            
                $location.path( "/login" );

            }, function (response) {
                status = response.status;
                if(status >= 500){
                    alert("something went wrong with server");
                }else if(status == 409){
                    alert("brand with this email id already exisits in our system");         
                }
            });
        }
    };
    
    $scope.getBrandProfileInfo = function(){
        
        //if currently logged user is brand and we have its email id then only call this api
        // get details from local storage if its empty then can't call this api
        // if we have user there then get details.
        // once we get that info store it in brandDetails variable and then no need to call this api again
        
        if ($scope.brandDetails == null){
            // get api set brandDetails value    
        }
        
    }



    $scope.getBrandProfileInfo();

$scope.count=0;

     $scope.records1 = [
         {path:"/static/images/searchFilterImages/animals.jpg", index: 0, class: "", label:"animals"},
         {path:"/static/images/searchFilterImages/art.jpg", index: 1, class: "", label:"art"},
         {path:"/static/images/searchFilterImages/books.jpg", index: 2, class: "", label:"books"},
         {path:"/static/images/searchFilterImages/science.jpg", index: 3, class: "", label:"science"},
         ]
     $scope.records2 = [
          {path:"/static/images/searchFilterImages/tech.jpg", index: 0, class: "", label:"tech"},
          {path:"/static/images/searchFilterImages/business.jpg", index: 1, class: "", label:"business"},
          {path:"/static/images/searchFilterImages/causes.jpg", index: 2, class: "", label:"causes"},
          {path:"/static/images/searchFilterImages/comedy.jpg", index: 3, class: "", label:"comedy"},
          ]
     $scope.records3 = [
          {path:"/static/images/searchFilterImages/dance.jpg", index: 0, class: "", label:"dance"},
          {path:"/static/images/searchFilterImages/sport.jpg", index: 1, class: "", label:"sport"},
          {path:"/static/images/searchFilterImages/education.jpg", index: 2, class: "", label:"education"},
          {path:"/static/images/searchFilterImages/style.jpg", index: 3, class: "", label:"style"},
          ]
     $scope.records4 = [
          {path:"/static/images/searchFilterImages/entertainment.jpg", index: 0, class: "", label:"entertainment"},
          {path:"/static/images/searchFilterImages/beauty.jpg", index: 1, class: "", label:"beauty"},
          {path:"/static/images/searchFilterImages/photograph.jpg", index: 2, class: "", label:"photograph"},
          {path:"/static/images/searchFilterImages/family.jpg", index: 3, class: "", label:"family"},
          ]
     $scope.records5 = [
          {path:"/static/images/searchFilterImages/fashion.jpg", index: 0, class: "", label:"fashion"},
          {path:"/static/images/searchFilterImages/fitness.jpg", index: 1, class: "", label:"fitness"},
          {path:"/static/images/searchFilterImages/tv.jpg", index: 2, class: "", label:"tv"},
          {path:"/static/images/searchFilterImages/film.jpg", index: 3, class: "", label:"film"},
          ]
      $scope.records6 = [
           {path:"/static/images/searchFilterImages/DIY.jpg", index: 0, class: "", label:"DIY"},
           {path:"/static/images/searchFilterImages/gaming.jpg", index: 1, class: "", label:"gaming"},
           {path:"/static/images/searchFilterImages/food.jpg", index: 2, class: "", label:"food"},
           {path:"/static/images/searchFilterImages/lifestyle.jpg", index: 3, class: "", label:"lifestyle"},
           ]
      $scope.records7 = [
           {path:"/static/images/searchFilterImages/politics.jpg", index: 0, class: "", label:"politics"},
           {path:"/static/images/searchFilterImages/news.jpg", index: 1, class: "", label:"news"},
           {path:"/static/images/searchFilterImages/journalism.jpg", index: 2, class: "", label:"journalism"},
           {path:"/static/images/searchFilterImages/travel.jpg", index: 3, class: "", label:"travel"},
           ]
      $scope.records8 = [
           {path:"/static/images/searchFilterImages/radio.jpg", index: 0, class: "", label:"radio"},
           {path:"/static/images/searchFilterImages/music.jpg", index: 1, class: "", label:"music"}
           ]




     //$scope.class= false;


     $scope.addClass1 = function(val){
            if($scope.records1[val].class === "activeone" )
                $scope.records1[val].class = "";
            else
                $scope.records1[val].class = "activeone";
            //console.log('response',records[val].index);
          }
     $scope.addClass2 = function(val){
             if($scope.records2[val].class === "activeone" )
                 $scope.records2[val].class = "";
             else
                 $scope.records2[val].class = "activeone";
             //console.log('response',records[val].index);
           }
     $scope.addClass3 = function(val){
             if($scope.records3[val].class === "activeone" )
                 $scope.records3[val].class = "";
             else
                 $scope.records3[val].class = "activeone";
             //console.log('response',records[val].index);
           }
     $scope.addClass4 = function(val){
             if($scope.records4[val].class === "activeone" )
                 $scope.records4[val].class = "";
             else
                 $scope.records4[val].class = "activeone";
             //console.log('response',records[val].index);
           }
     $scope.addClass5 = function(val){
             if($scope.records5[val].class === "activeone" )
                 $scope.records5[val].class = "";
             else
                 $scope.records5[val].class = "activeone";
             //console.log('response',records[val].index);
           }
     $scope.addClass6 = function(val){
             if($scope.records6[val].class === "activeone" )
                 $scope.records6[val].class = "";
             else
                 $scope.records6[val].class = "activeone";
             //console.log('response',records[val].index);
           }
     $scope.addClass7 = function(val){
             if($scope.records7[val].class === "activeone" )
                 $scope.records7[val].class = "";
             else
                 $scope.records7[val].class = "activeone";
             //console.log('response',records[val].index);
           }
     $scope.addClass8 = function(val){
             if($scope.records8[val].class === "activeone" )
                 $scope.records8[val].class = "";
             else
                 $scope.records8[val].class = "activeone";
             //console.log('response',records[val].index);
           }

       $scope.addClass = function(i){
                   if($scope.influencers[i].class === "pic-container-sel" )
                       $scope.influencers[i].class = "pic-container";
                   else
                       $scope.influencers[i].class = "pic-container-sel";
                   //console.log('response',records[val].index);
                 }


        $scope.influencers=[];
        $scope.influTempData=[];

              $scope.searchInfluencer = function() {

                  $scope.areas=[];

                  for (var i=0; i<4; i++) {
                        if($scope.records1[i].class === "activeone")
                              $scope.areas.push($scope.records1[i].label);
                      }
                  for (var i=0; i<4; i++) {
                        if($scope.records2[i].class === "activeone")
                              $scope.areas.push($scope.records2[i].label);
                      }
                  for (var i=0; i<4; i++) {
                        if($scope.records3[i].class === "activeone")
                              $scope.areas.push($scope.records3[i].label);
                      }
                  for (var i=0; i<4; i++) {
                        if($scope.records4[i].class === "activeone")
                              $scope.areas.push($scope.records4[i].label);
                      }
                  for (var i=0; i<4; i++) {
                        if($scope.records5[i].class === "activeone")
                              $scope.areas.push($scope.records5[i].label);
                      }
                  for (var i=0; i<4; i++) {
                        if($scope.records6[i].class === "activeone")
                              $scope.areas.push($scope.records6[i].label);
                      }
                  for (var i=0; i<4; i++) {
                        if($scope.records7[i].class === "activeone")
                              $scope.areas.push($scope.records7[i].label);
                      }
                  for (var i=0; i<2; i++) {
                        if($scope.records8[i].class === "activeone")
                              $scope.areas.push($scope.records8[i].label);
                      }

                  var data2 ={
                              "start" : parseInt($scope.from),
                              "end" : parseInt($scope.to),
                              "gender": $scope.gender,
                              "areas_of_interest" : $scope.areas
                             }

                 $http.post('http://localhost:5000/brand/brandGetInfluencers', data2).then(function (response2) {

                                 if (response2.data){
                                     $scope.influencers=response2.data.data;
                                     //console.log(response2.data);

                                 for (var i=0;i<$scope.influencers.length;i++)
                                     {
                                         $scope.influencers[i].class="pic-container"
                                     }

                                     console.log($scope.influencers);
                                     //$scope.showCards.hide('show')

                                     //$scope.showCards=true;
                                 }

                             }, function (response) {
                                 status = response.status;
                                 if(status >= 500){
                                     alert("something went wrong with server");
                                 }else if(status == 404){
                                     alert("Influencer do not exisits");
                                 }
                             });

               }

               $scope.submitCampRequest = function() {

                       $scope.influData=[]
                       for (var i=0;i<$scope.influencers.length;i++)
                            {
                                if($scope.influencers[i].class === "pic-container-sel")
                                    $scope.influData.push($scope.records3[i].label);
                            }
                       var data3 =
                           {
                               "campaign_name" : $scope.campaignName,
                               "email" : $scope.campaignEmail,
                               "campaign_info_rqmts" : $scope.cInfo,
                               "requested_influencers" : $scope.influData
                           }

                       $http.post('http://localhost:5000/brandcampaignrequest', data3).then(function (response3) {

                           if (response3.data)

                               console.log($scope.msg);
                           console.log("Added to the database");
                           $location.path( "/blogin" );

                       }, function (response3) {

                           $scope.msg = "Service not Exists";

                           $scope.statusval = response3.status;

                           $scope.statustext = response3.statusText;

                           $scope.headers = response3.headers();

                       });
                   };






});