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
    $routeProvider.when('/', {
        templateUrl: '../static/partials/home.html',
        controller: "indexController"
    }).when('/brand', {
        templateUrl: '../static/partials/brand.html',
        controller: "indexController"
    }).when('/influencer', {
        templateUrl: '../static/partials/influencer.html',
        controller: "indexController"
    }).when('/login', {
        templateUrl: 'static/partials/login.html',
        controller: "indexController"
    }).otherwise({
        redirectTo: '/'
    })
}]);