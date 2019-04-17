
var brandController = app.controller("brandController", function ($scope, $window) {

    
    
    $scope.update = function() {
        console.log($scope.socialhandles);
        

        var data =
        {
            "company_name" : $scope.cname,
            "email" : $scope.email,
            "password" : $scope.num,
            "address" : "tempe"
        }



        $http.post('http://localhost:5000/brand', data).then(function (response) {

            if (response.data)

                $scope.msg = "Post Data Submitted Successfully!";

        }, function (response) {

            $scope.msg = "Service not Exists";

            $scope.statusval = response.status;

            $scope.statustext = response.statusText;

            $scope.headers = response.headers();

        });

    };

    
    
});

