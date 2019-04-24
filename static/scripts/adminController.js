app.controller("adminController", function ($scope, $window, $http, $location) {

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

    $http.get("http://localhost:5000/brandcampaignrequest")
        .then(function(response) {
        $scope.campaignData = response.data;
    });



    // if logged in then only call this
    $scope.searchBrands();

    $scope.approveCampaign = function(){

        var data =
            {
                "campaign_name" : $scope.cname,
                "email" : $scope.bname,
                "status": false
            }


        $http.post('http://localhost:5000/brandcampaignrequestapprove', data).then(function (response) {
            data = response.data;
            console.log(data);
            //$scope.brands = $scope.brands.filter(item => item !== $scope.brand);

        }, function (errResponse) {
            console.log(errResponse);
        });

    }

    $scope.denyCampaign = function(){

        var data =
            {
                "campaign_name" : $scope.cname,
                "email" : $scope.bname,
                "status": false
            }


        $http.post('http://localhost:5000/brandcampaignrequestapprove', data).then(function (response) {
            data = response.data;
            console.log(data);
            //$scope.brands = $scope.brands.filter(item => item !== $scope.brand);

        }, function (errResponse) {
            console.log(errResponse);
        });

    }



});