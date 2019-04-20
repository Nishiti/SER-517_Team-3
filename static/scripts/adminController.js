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
        
        data = {
          "email" : brand.email  
        };
        
        $scope.brands.splice(i, 1);
        
        
        $http.post('http://localhost:5000/admin/removebrand', data).then(function (response) {
            data = response.data;
            console.log(data);
            //$scope.brands = $scope.brands.filter(item => item !== $scope.brand);
            
        }, function (errResponse) {
            console.log(errResponse);
        });        
        
    }

    $http.get("http://localhost:5000/brandcampaignrequest")
      .then(function(response) {
          $scope.campaignData = response.data;
      });

    



});