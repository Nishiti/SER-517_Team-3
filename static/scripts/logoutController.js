app.controller("logoutController", function ($http, $scope, $window, $location) {

    $scope.logout = function(){


        if ($window.confirm("Are you sure?")) {
            console.log("logout called!");
            $window.localStorage.removeItem('nxtlabUser');
            $http.defaults.headers.common.Authorization = '';
            $scope.needlogin = true;
            // call logout apis
            $location.path( "/login" );
            
        } else {
            console.log("logout cancled");
            $location.path("/home");
        }



    }

    $scope.logout();

});

