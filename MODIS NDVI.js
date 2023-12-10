
var dataset = ee.ImageCollection("MODIS/061/MOD13Q1")
  .filterDate('2020-01-01', '2020-12-31')
  .select('NDVI');

var provinces = SMMR; 


print(dataset);

var ndviData = dataset.map(function(image) {
var scaledNDVI = image.select('NDVI').multiply(0.0001);
  return scaledNDVI.clip(provinces);
});

var NDVImean = ndviData.mean();


var visParams = {
  min: -1,
  max: 1,
  palette: ['FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718', '74A901', '66A000', '529400', '3E8601', '207401', '056201', '004C00', '023B01', '012E01', '011D01', '011301'],
};

Map.addLayer(NDVImean, visParams, 'Mean NDVI');





