# průvodní list pro semenný materiál
### čtení dat z fotky vyplněného formuláře 

testování curl (test/testImage**.jpg):

`curl -i -X POST -H "Content-Type: multipart/form-data" -F "image=@test/testImageSeed.jpg" http://0.0.0.0:5000/seedMaterial  `

