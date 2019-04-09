var app = angular.module('mainApp', []);


app.controller('myCtrl', function($scope,$http) {


    $scope.login = function() {
        
        
        
        var data = {
            "email" : $scope.email,
            "password" : $scope.password
        };


        $http.post('http://localhost:5000/admin/signin', data).then(function (response) {

            if (response.data){
                
                console.log(response);
                
                
                
            }

        }, function (response) {

            $scope.msg = "Service not Exists";

            $scope.statusval = response.status;

            $scope.statustext = response.statusText;

            $scope.headers = response.headers();

        });

    };

});
