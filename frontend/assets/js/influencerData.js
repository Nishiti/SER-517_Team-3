var app = angular.module('app', []);
app.directive("matchPassword", function () {
    return {
        require: "ngModel",
        scope: {
            otherModelValue: "=matchPassword"
        },
        link: function(scope, element, attributes, ngModel) {

            ngModel.$validators.matchPassword = function(modelValue) {
                return modelValue == scope.otherModelValue;
            };

            scope.$watch("otherModelValue", function() {
                ngModel.$validate();
            });
        }
    };
});

app.controller('myCtrl', function($scope,$http) {
    //console.log($scope.cname)

    $scope.update = function() {
        console.log($scope.fname);
        console.log($scope.lname);
        console.log($scope.email);
        console.log($scope.password);
        console.log($scope.confirm_password);
        console.log($scope.cname);
        console.log($scope.cname);
        console.log($scope.cname);
        console.log($scope.cname);

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





    //    .then(function(response) {  //Success

          //  $scope.content = response.data;
        //}, function(response) {     //Failure
        //    $scope.content = "Something went wrong";
        //});
