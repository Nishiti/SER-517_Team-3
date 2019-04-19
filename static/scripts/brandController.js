
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
app.controller("createCampaignController", function ($scope, $window)
{
 var data =
         {
             "campaignName" : $scope.campaignName,
             "last_name" : $scope.lname,
             "email" : $scope.email,
             "password" : $scope.password,
             "confirm_password" : $scope.confirm_password,
             "big_deal_on_option1" : $scope.website,
             "big_deal_on_option2" : $scope.insta,
             "big_deal_on_option3" : $scope.youtube,
             "big_deal_on_option4" : $scope.facebook,
             "big_deal_on_option5" : $scope.other,
             "website_social_media_handles" : $scope.socialmedia,
             "followers" : $scope.followers,
             "areas": $scope.areas

         }

         $http.post('http://localhost:5000/influencer/signup', data).then(function (response) {

             if (response.data)

                 $scope.msg = "Post Data Submitted Successfully!";

         }, function (response) {

             $scope.msg = "Service not Exists";

             $scope.statusval = response.status;

             $scope.statustext = response.statusText;

             $scope.headers = response.headers();

         });

     });

