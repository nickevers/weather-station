import React, { useEffect, useState } from 'react';
import { ActivityIndicator, FlatList, Text, View, TouchableOpacity } from 'react-native';

function renderItem(item) {
  return (
      <TouchableOpacity  
               style={{flex:1/2,
               aspectRatio:1,
               backgroundColor: 'blue',
               margin: 4,
               justifyContent: 'center', //Centered vertically
               alignItems: 'center', // Centered horizontally
               }}>
              <Text>{item.title}, {item.releaseYear}</Text>
      </TouchableOpacity>
  )
}

export default App = () => {
  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([]);

  

  useEffect(() => {
    fetch('https://reactnative.dev/movies.json')
      .then((response) => response.json())
      .then((json) => setData(json.movies))
      .catch((error) => console.error(error))
      .finally(() => setLoading(false));
  }, []);

  return (
    <View style={{ flex: 1, paddingLeft: 8, paddingRight: 8, paddingTop: 24, backgroundColor: 'dimgray', textAlign: 'center' }}>
      {isLoading ? <ActivityIndicator/> : (
        <FlatList
        numColumns={2}
          data={data}
          keyExtractor={({ id }, index) => id}
          renderItem={({ item }) => renderItem(item)}
        />
      )}
    </View>
  );
};