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
            console.log(response.data.data);

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
        console.log(respose.data);
        console.log(response.data.data);

    }, function (errResponse) {
        console.log(errResponse);
    });

}
$scope.searchCampaigns();
});