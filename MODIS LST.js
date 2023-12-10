//Area of Interest and Date Duration
var area = SMMR
var start_date = '2001-01-01';
var end_date = '2002-01-01';

var modis = ee.ImageCollection("MODIS/061/MOD11A1")
.filterBounds(area)
.filterDate(start_date, end_date)
.select('LST_Day_1km')
.map(function(a) {
  return a.set('month', ee.Image(a).date().get('month'));
});
print(modis);
var months = ee.List(modis.aggregate_array('month')).distinct();
// print(months);
var mc = months.map(function(x){
  return modis.filterMetadata('month', 'equals', x).mean().set('month',x)
})
var monthly_mean = ee.ImageCollection.fromImages(mc)

//Convert to Celsius
var LSTday = modis.map(function(image){
  return image
  .multiply(0.02)
  .subtract(273.15)
  .copyProperties(image, ['system:time_start']);
  });
  
  //Getting the Mean
  var LSTmean= LSTday.mean().clip(SMMR);
  var meanValue = LSTmean.reduceRegion({
  reducer: ee.Reducer.mean(),
  geometry: area,
  scale: 1000,
  maxPixels: 1e13
});
print('Mean LST value:', meanValue.get('LST_Day_1km'));


  Map.addLayer(LSTmean, {
    min:20, max:40,
    palette: ['blue', 'limegreen', 'yellow', 'darkorange', 'red']});
    