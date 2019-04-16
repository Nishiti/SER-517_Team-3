// index contorller will deal with only functions required on index page
var indexController = app.controller("indexController", function ($scope, $window, $http,$location) {

    $scope.companyName = "nxstlab";
    
    function checkIfSessionActive(){
        
        return false;
        
    }
    
    

    $scope.login = function(){

        var email = $scope.email;
        var password = $scope.password;

        var data = {
            'email' : email,
            'password' : password
        };

        $http.post('http://localhost:5000/admin/signin', data).then(function (response) {
            
            
            data = response.data;
            console.log(data);
            var temp = {
                'access_token':data.access_token,
                'email' : data.email,
                'refresh_token' : data.refresh_token,
                'role' : data.role
            };
            
            $window.localStorage.nxtlabUser = JSON.stringify(temp);
            $scope.logged = true;
            $http.defaults.headers.common.Authorization = 'Bearer ' + data.access_token;
            
            
//        $http.get('http://localhost:5000/admin/secret').then(function (response) {
//            data = response.data;
//            console.log(data);
//        }, function (errResponse) {
//            console.log(errResponse);
//        });
            
            if(data.role == "admin"){
               $location.path( "/admin" );
            }
                
        }, function (errResponse) {
            console.log(errResponse);
        });
        
    };
    
    $scope.logout = function(){
        console.log("logout called!");
        $window.localStorage.removeItem('nxtlabUser');
        // call logout apis
        $location.path( "/" );
    }
    
    $window.localStorage.removeItem('nxtlabUser');

    
    
});
