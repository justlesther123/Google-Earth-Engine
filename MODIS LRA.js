var temp = ee.ImageCollection("MODIS/061/MOD11A1")
      .filterDate('2010-01-01', '2011-01-01')
      .select('LST_Day_1km')
      .mean()
      .multiply(0.02)
      .subtract(273.15)
      .rename('temperature')
      
var vegetation = ee.ImageCollection("MODIS/061/MOD13A2")
.filterDate('2010-01-01', '2011-01-01')
  .select('NDVI');
  var ndviData = vegetation.map(function(image) {
  var scaledNDVI = image.select('NDVI').multiply(0.0001);
  return scaledNDVI.clip(SMMR);
});
print(vegetation);
var NDVImean = ndviData.mean();

var combine = temp.addBands(NDVImean);

var scale = Map.getScale()
var values = combine.sample({
  region:SMMR,
  scale:scale,
  numPixels: 5000,
  geometries: true
})
print(values);

Map.addLayer(values, {}, 'sample')


var temp = ee.ImageCollection("MODIS/061/MOD11A1")
      .filterDate('2001-01-01', '2005-01-01')
      .select('LST_Day_1km')
      .mean()
      .multiply(0.02)
      .subtract(273.15)
      .rename('temperature')
      
var vegetation = ee.ImageCollection("MODIS/061/MOD13A2")
.filterDate('2001-01-01', '2005-01-01')
  .select('NDVI');
  var ndviData = vegetation.map(function(image) {
  var scaledNDVI = image.select('NDVI').multiply(0.0001);
  return scaledNDVI.clip(SMMR);
});

var NDVImean = ndviData.mean();

var combine = temp.addBands(NDVImean);

var scale = Map.getScale()
var values = combine.sample({
  region:SMMR,
  scale:scale,
  numPixels: 5000,
  geometries: true
})
print(values);

Map.addLayer(values, {}, 'sample')




var featureCollection = ee.FeatureCollection(values.map(function (feature) {
  var geometry = feature.geometry();
  var NDVI = feature.getNumber('NDVI');
  var temperature = feature.getNumber('temperature');

  
  if (geometry !== null && NDVI !== null && temperature !== null) {
    return ee.Feature(geometry, {
      NDVI: NDVI,
      temperature: temperature
    });
  } else {
    return null; 
  }
}).filter(ee.Filter.notNull(['NDVI', 'temperature'])));

