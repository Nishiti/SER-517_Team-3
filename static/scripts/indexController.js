var indexController = app.controller("indexController", function ($scope, $window, $http,$location) {

    $window.localStorage.needlogin = "true";
    $scope.showUnauthorozed = false;
    $scope.showNotFound = false;
    $scope.companyName = "nxstlab";
    
    
    $scope.login = function(){
        $scope.showUnauthorozed = false;
        $scope.showNotFound = false;
        var email = $scope.email;
        var password = $scope.password;

        var data = {
            'email' : email,
            'password' : password
        };

        $http.post('http://localhost:5000/user/signin', data).then(function (response) {
            
            data = response.data;
            console.log(data);
            var temp = {
                'access_token':data.access_token,
                'email' : data.email,
                'refresh_token' : data.refresh_token,
                'role' : data.role
            };
            
            $window.localStorage.nxtlabUser = JSON.stringify(temp);
            $window.localStorage.needlogin = "false";
            $http.defaults.headers.common.Authorization = 'Bearer ' + data.access_token;
            
                        
            if(data.role == "admin"){
               $location.path( "/admin" );
            }else if(data.role == "brand"){
                $location.path("/blogin");
            }else if(data.role == "influencer") {
                $location.path("/ilogin");
            }
                
        }, function (errResponse) {
            console.log(errResponse);
            status = errResponse.status;
            if(status >= 500){
                 alert("something went wrong with server");
            }else if(status == 404){
                $scope.showNotFound = true;     
            }else if(status == 401){
                $scope.showUnauthorozed = true;
            }
        });
        
    };
    
    
});
