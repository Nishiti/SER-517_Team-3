app.controller("adminController", function ($scope, $window, $http, $location) {
    $scope.login = function checkIfLoginActive(){

        //console.log($window.localStorage.nxtlabUser);
        console.log($window.localStorage.needlogin);
        //if($location.path() ==/)
        var currentpath = $location.path();
        console.log(currentpath);
        if (currentpath == "/admin" || currentpath == "/home") {

        }else{
            if ($window.localStorage.needlogin == "true") {
                $location.path("/login")
            }
        }

    };

    $scope.login();
   

    $scope.searchBrands = function(){

        if ($scope.brandName == undefined){
            $scope.brandName = "";
        }

        $scope.filterBrand = {
            'company_name' : $scope.brandName
        };

        $http.post('http://localhost:5000/admin/getBrands', $scope.filterBrand).then(function (response) {
            $scope.brands = response.data.data;

        }, function (errResponse) {
            console.log(errResponse);
        });

    }

    $scope.searchInfluencers = function(){

        if ($scope.influencerName == undefined){
            $scope.influencerName = "";
        }

        $scope.filterInfluencers = {
            'name' : $scope.influencerName
        };

        $http.post('http://localhost:5000/admin/getInfluencers', $scope.filterInfluencers).then(function (response) {
            $scope.influencers = response.data.data;

        }, function (errResponse) {
            console.log(errResponse);
        });

    }

    $scope.removeInfluencer = function(i){
        var influencer = $scope.influencers[i];

        data = {
            "email" : influencer.email
        };

        $scope.influencers.splice(i, 1);


        $http.post('http://localhost:5000/admin/removeInfluencers ', data).then(function (response) {
            data = response.data;
            console.log(data);
            //$scope.brands = $scope.brands.filter(item => item !== $scope.brand);

        }, function (errResponse) {
            console.log(errResponse);
        });

    }


    $scope.adminSignup = function(){

        var email = $scope.adminemail;
        var password = $scope.adminpassword;

        var data = {
            'first_name' : email,
            'last_name' : email,
            'email' : email,
            'password' : password
        };

        $http.post('http://localhost:5000/admin/signup', data).then(function (response) {
            data = response.data;
            console.log(data);
            $location.path( "/login" );

        }, function (errResponse) {
            console.log(errResponse);
        });

    };

    $scope.removeBrand = function(i){

        var brand = $scope.brands[i];

        var data = {
            "email" : brand.email  
        };

        $scope.brands.splice(i, 1);

        $http.post('http://localhost:5000/admin/removebrand', data).then(function (response) {
            data = response.data;
            console.log(data);
        }, function (response) {
            status = response.status;
            if(status >= 500){
                alert("Something went wrong with server");
            }else if(status == 404){
                alert("This brand does not exisits in system");         
            }
        });        

    }

    $scope.searchBrands();

    $scope.brandData=[];
    $scope.brandTempData=[];
    $http.get("http://localhost:5000/brand")
            .then(function(response) {
            $scope.brandTempData = response.data;
            for (var i=0;i<$scope.brandTempData.length;i++)
                {
                    if ($scope.brandTempData[i].isapproved === false)
                        $scope.brandData.push($scope.brandTempData[i])
                }
        });


    $scope.approveBrand = function(x){
            var data =
                     {"campaign_name" : x.company_name,
                      "email" : x.email,
                      "isapproved": true
                     }
            var index=$scope.brandData.indexOf(x)
                                  $scope.brandData.splice(index,1);

            $http.post('http://localhost:5000/admin/approve/brandsingup', data).then(function (response) {
                data = response.data;
                console.log(data);
            }, function (errResponse) {
                console.log(errResponse);
            });
    }

    $scope.denyBrand = function(x){
                var data =
                         {"company_name" : x.company_name,
                          "email" : x.email,
                         }
                var index=$scope.brandData.indexOf(x)
                          $scope.brandData.splice(index,1);

        $http.post('http://localhost:5000/admin/removebrand', data).then(function (response) {
            data = response.data;
            console.log(data);
        }, function (errResponse) {
            console.log(errResponse);
        });
    }

    $scope.campaignData=[];
    $http.get("http://localhost:5000/brandcampaignrequest")
        .then(function(response) {
        $scope.campaignData = response.data;
    });

    $scope.approveCampaign = function(x){
            var data =
                     {"campaign_name" : x.campaign_name,
                      "email" : x.email,
                      "status": true
                     }
            var index=$scope.campaignData.indexOf(x)
                                  $scope.campaignData.splice(index,1);

            $http.post('http://localhost:5000/brandcampaignrequestapprove', data).then(function (response) {
                data = response.data;
                console.log(data);
            }, function (errResponse) {
                console.log(errResponse);
            });
    }



    $scope.denyCampaign = function(x){
                var data =
                         {"campaign_name" : x.campaign_name,
                          "email" : x.email,
                          "status": false
                         }
                var index=$scope.campaignData.indexOf(x)
                          $scope.campaignData.splice(index,1);

        $http.post('http://localhost:5000/brandcampaignrequestapprove', data).then(function (response) {
            data = response.data;
            console.log(data);
        }, function (errResponse) {
            console.log(errResponse);
        });
    }


$scope.searchCampaigns = function(){

    // if ($scope.campaignName == undefined){
    //     $scope.campaignName = "";
    // }

    // $scope.filterCampaign = {
    //     'campaign_name' : $scope.campaignName
    // };
    $scope.campaigns = []
    $http.get('http://localhost:5000/approvecamp').then(function (response) {
        $scope.campaigns = response.data.data;


    }, function (errResponse) {
        console.log(errResponse);
    });

}
$scope.searchCampaigns();


     $scope.count=0;

     $scope.records1 = [
         {path:"/static/images/searchFilterImages/animals.jpg", index: 0, class: "", label:"animals"},
         {path:"/static/images/searchFilterImages/art.jpg", index: 1, class: "", label:"art"},
         {path:"/static/images/searchFilterImages/books.jpg", index: 2, class: "", label:"books"},
         {path:"/static/images/searchFilterImages/science.jpg", index: 3, class: "", label:"science"},
         ]

         console.log($scope.records1);
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

});