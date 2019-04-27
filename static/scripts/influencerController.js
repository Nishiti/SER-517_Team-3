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


app.controller("influencerController", function ($scope, $window, $http, $location)
{
    $scope.login = function checkIfLoginActive(){

        //console.log($window.localStorage.nxtlabUser);
        console.log($window.localStorage.needlogin);
        //if($location.path() ==/)
        var currentpath = $location.path();
        console.log(currentpath);
        if (currentpath == "/influencer" || currentpath == "/home") {

        }else{
            if ($window.localStorage.needlogin == "true") {
                $location.path("/login")
            }
        }

    };

    $scope.login();

    $scope.count=0;

    $scope.records1 = [
        {path:"/static/images/searchFilterImages/animals.jpg", index: 0, class: "", label:"animals"},
        {path:"/static/images/searchFilterImages/art.jpg", index: 1, class: "", label:"art"},
        {path:"/static/images/searchFilterImages/books.jpg", index: 2, class: "", label:"books"},
        {path:"/static/images/searchFilterImages/science.jpg", index: 3, class: "", label:"science"},
    ]
    $scope.records2 = [
        {path:"/static/images/searchFilterImages/tech.jpg", index: 0, class: "", label:"tech"},
        {path:"/static/images/searchFilterImages/business.jpg", index: 1, class: "", label:"business"},
        {path:"/static/images/searchFilterImages/causes.jpg", index: 2, class: "", label:"causes"},
        {path:"/static/images/searchFilterImages/comedy.jpg", index: 3, class: "", label:"comedy"},
    ]
    $scope.records3 = [
        {path:"/static/images/searchFilterImages/dance.jpg", index: 0, class: "", label:"dance"},
        {path:"/static/images/searchFilterImages/sport.jpg", index: 1, class: "", label:"sport"},
        {path:"/static/images/searchFilterImages/education.jpg", index: 2, class: "", label:"education"},
        {path:"/static/images/searchFilterImages/style.jpg", index: 3, class: "", label:"style"},
    ]
    $scope.records4 = [
        {path:"/static/images/searchFilterImages/entertainment.jpg", index: 0, class: "", label:"entertainment"},
        {path:"/static/images/searchFilterImages/beauty.jpg", index: 1, class: "", label:"beauty"},
        {path:"/static/images/searchFilterImages/photograph.jpg", index: 2, class: "", label:"photograph"},
        {path:"/static/images/searchFilterImages/family.jpg", index: 3, class: "", label:"family"},
    ]
    $scope.records5 = [
        {path:"/static/images/searchFilterImages/fashion.jpg", index: 0, class: "", label:"fashion"},
        {path:"/static/images/searchFilterImages/fitness.jpg", index: 1, class: "", label:"fitness"},
        {path:"/static/images/searchFilterImages/tv.jpg", index: 2, class: "", label:"tv"},
        {path:"/static/images/searchFilterImages/film.jpg", index: 3, class: "", label:"film"},
    ]
    $scope.records6 = [
        {path:"/static/images/searchFilterImages/DIY.jpg", index: 0, class: "", label:"DIY"},
        {path:"/static/images/searchFilterImages/gaming.jpg", index: 1, class: "", label:"gaming"},
        {path:"/static/images/searchFilterImages/food.jpg", index: 2, class: "", label:"food"},
        {path:"/static/images/searchFilterImages/lifestyle.jpg", index: 3, class: "", label:"lifestyle"},
    ]
    $scope.records7 = [
        {path:"/static/images/searchFilterImages/politics.jpg", index: 0, class: "", label:"politics"},
        {path:"/static/images/searchFilterImages/news.jpg", index: 1, class: "", label:"news"},
        {path:"/static/images/searchFilterImages/journalism.jpg", index: 2, class: "", label:"journalism"},
        {path:"/static/images/searchFilterImages/travel.jpg", index: 3, class: "", label:"travel"},
    ]
    $scope.records8 = [
        {path:"/static/images/searchFilterImages/radio.jpg", index: 0, class: "", label:"radio"},
        {path:"/static/images/searchFilterImages/music.jpg", index: 1, class: "", label:"music"}
    ]


    $scope.addClass1 = function(val){
        if($scope.records1[val].class === "activeone" )
            $scope.records1[val].class = "";
        else
            $scope.records1[val].class = "activeone";
        //console.log('response',records[val].index);
    }
    $scope.addClass2 = function(val){
        if($scope.records2[val].class === "activeone" )
            $scope.records2[val].class = "";
        else
            $scope.records2[val].class = "activeone";
        //console.log('response',records[val].index);
    }
    $scope.addClass3 = function(val){
        if($scope.records3[val].class === "activeone" )
            $scope.records3[val].class = "";
        else
            $scope.records3[val].class = "activeone";
        //console.log('response',records[val].index);
    }
    $scope.addClass4 = function(val){
        if($scope.records4[val].class === "activeone" )
            $scope.records4[val].class = "";
        else
            $scope.records4[val].class = "activeone";
    }
    $scope.addClass5 = function(val){
        if($scope.records5[val].class === "activeone" )
            $scope.records5[val].class = "";
        else
            $scope.records5[val].class = "activeone";
        //console.log('response',records[val].index);
    }
    $scope.addClass6 = function(val){
        if($scope.records6[val].class === "activeone" )
            $scope.records6[val].class = "";
        else
            $scope.records6[val].class = "activeone";
        //console.log('response',records[val].index);
    }
    $scope.addClass7 = function(val){
        if($scope.records7[val].class === "activeone" )
            $scope.records7[val].class = "";
        else
            $scope.records7[val].class = "activeone";
        //console.log('response',records[val].index);
    }
    $scope.addClass8 = function(val){
        if($scope.records8[val].class === "activeone" )
            $scope.records8[val].class = "";
        else
            $scope.records8[val].class = "activeone";
    }


    $scope.influencers=[];
    $http.get("http://localhost:5000/brandcampaignrequest")
        .then(function(response) {
            $scope.campaignData = response.data;
        });

    $scope.updateinflu = function() {

        $scope.areas=[];
        $scope.big_deal={"website":false, "insta":false, "youtube": false, "facebook": false, "other":false};

//        for(record: records1){
//             if(record.class === "activeone")
//                 $scope.areas.push(x.label);
//            }

        for (var i=0; i<4; i++) {
            if($scope.records1[i].class === "activeone")
                $scope.areas.push($scope.records1[i].label);
        }
        for (var i=0; i<4; i++) {
            if($scope.records2[i].class === "activeone")
                $scope.areas.push($scope.records2[i].label);
        }
        for (var i=0; i<4; i++) {
            if($scope.records3[i].class === "activeone")
                $scope.areas.push($scope.records3[i].label);
        }
        for (var i=0; i<4; i++) {
            if($scope.records4[i].class === "activeone")
                $scope.areas.push($scope.records4[i].label);
        }
        for (var i=0; i<4; i++) {
            if($scope.records5[i].class === "activeone")
                $scope.areas.push($scope.records5[i].label);
        }
        for (var i=0; i<4; i++) {
            if($scope.records6[i].class === "activeone")
                $scope.areas.push($scope.records6[i].label);
        }
        for (var i=0; i<4; i++) {
            if($scope.records7[i].class === "activeone")
                $scope.areas.push($scope.records7[i].label);
        }
        for (var i=0; i<2; i++) {
            if($scope.records8[i].class === "activeone")
                $scope.areas.push($scope.records8[i].label);
        }

        var data =
            {
                "first_name" : $scope.fname,
                "last_name" : $scope.lname,
                "email" : $scope.email,
                "password" : $scope.password,
                "confirm_password" : $scope.confirm_password,
                "big_deal_on_option1" : $scope.big_deal.website,
                "big_deal_on_option2" : $scope.big_deal.insta,
                "big_deal_on_option3" : $scope.big_deal.youtube,
                "big_deal_on_option4" : $scope.big_deal.facebook,
                "big_deal_on_option5" : $scope.big_deal.other,
                "website_social_media_handles" : $scope.socialmedia,
                "followers" : $scope.followers,
                "areas_of_interest": $scope.areas,
                "gender": $scope.gender,
                "dob": $scope.dob
            }
        $http.post('http://localhost:5000/influencer/signup', data).then(function (response) {

            if (response.data)

                $scope.msg = "Post Data Submitted Successfully!";
            $location.path( "/login" );

        }, function (response) {
            status = response.status;
            if(status >= 500){
                alert("something went wrong with server");
            }else if(status == 409){
                alert("Influencer with this email id already exisits");
            }
        });

    };

    $scope.getInfProfileInfo = function(){
            
            var sessionDetails = $window.localStorage.nxtlabUser
            
            if(sessionDetails != null && sessionDetails.length > 0){

                var user = JSON.parse(sessionDetails);    
                var useremail = user.email;
                
                var data = {
                  "email" : useremail
                };
                
                $http.post('http://localhost:5000/influencer/profile', data).then(function (response) {

                if (response.data){
                    console.log("this is my response");
                    var data = response.data.data;
                    console.log(data);
                    $scope.firstname = data.first_name;
                    $scope.lastname = data.last_name;
                    $scope.handle = data.website_social_media_handles;
                    $scope.followers = data.followers;
                    $scope.password = data.password;
                    $scope.profileImage = data.image;
                    $scope.cimage = data.campaignImage;
                    $scope.email = data.email;

                }

            }, function (response) {
                status = response.status;
                if(status >= 500){
                    alert("something went wrong with server");
                }else if(status == 404){
                    alert("Influencer do not exisits");
                }
            });
                
            }
            
        }
        $scope.getInfProfileInfo();


});