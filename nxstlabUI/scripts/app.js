var app = angular.module("mainApp", ["ngRoute"]);

// index contorller will deal with only functions required on index page
var indexController = app.controller("indexController", function ($scope, $window) {

    $scope.companyName = "nxstlab";
    
    $scope.popupGreet = function(){
        $window.alert("Hi there " + $scope.companyName);
    };    
    
});

var brandController = app.controller("brandController", function ($scope, $window) {

    
});


var brandController = app.controller("influencerController", function ($scope, $window) {

    
});


var brandController = app.controller("loginController", function ($scope, $window) {

    
});



app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/brand', {
        templateUrl: "/views/brand.html",
        controller: "brandController"
    }).when('/influencer', {
        templateUrl: "/views/influencer.html",
        controller: "influencerController"
    }).when('/login', {
        templateUrl: "/views/login.html",
        controller: "loginController"
    }).otherwise({
        templateUrl: "/views/home.html",
        controller: "indexController"
    })
}]);