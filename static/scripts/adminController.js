app.controller("adminController", function ($scope, $window, $http, $location) {

    $scope.searchBrands = function(){
        $scope.filterBrand = {};

        $http.post('http://localhost:5000/admin/getBrands', $scope.filterBrand).then(function (response) {
            $scope.brands = response.data.data;

//            var brand = [{
//                company_name: "Brand 1",
//                email: "abc@xyz.com",
//                address: "Collab",
//            }, {
//                company_name: "Brand 2",
//                email: "abc@xyz.com",
//                address: "Gifting",
//            }, {
//                company_name: "Brand 3",
//                email: "abc@xyz.com",
//                address: "Digital Strategy",
//            }];

            //console.log($scope.brands);

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
    
    
    $scope.searchBrands();


});