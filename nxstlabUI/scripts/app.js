var app = angular.module("mainApp", ["ngRoute"]);

// index contorller will deal with only functions required on index page
var indexController = app.controller("indexController", function ($scope, $window) {

    $scope.companyName = "nxstlab";
    
    $scope.attack = function () {
        
        
        $window.alert("Hi there " + $scope.companyName);
    };    
    
});

app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/login', {
        templateUrl: "/views/login.html",
        controller: "loginController"
    }).otherwise({
        templateUrl: "/views/home.html",
        controller: "indexController"
    })
}]);
