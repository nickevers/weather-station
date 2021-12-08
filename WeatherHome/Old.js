import React, { useEffect, useState } from 'react';
import { Text, View, TouchableOpacity, StyleSheet, ActivityIndicator, FlatList, Button , Modal, TextInput} from 'react-native';
import { SimpleLineIcons } from '@expo/vector-icons'; 


export default App = () => {
  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([{'measurement': 0, 'unit': '℃' }, 
  {'measurement': 0, 'unit':'%'},
  {'measurement': 0, 'unit': 'hPa'},
  {'measurement': 0, 'unit': 'M/s'},
  {'measurement': 0, 'unit': 'M/s'},
  {'measurement': 0, 'unit': ''},
  {'measurement': 0, 'unit': 'mm/u'},
  {'measurement': '-1', 'unit': 'settings'},]);
  const [menu, setMenu] = useState(false);
  const [ip, onChangeIp] = useState('http://192.68.2.88:5000');
  const enterMenu = () => setMenu(true);
  

  useEffect(() => {
    intervalId = setInterval(() => {
      fetch(ip+'/current')
      .then((response) => response.json())
      .then((json) => setData([{'measurement': json[0].AIR_TEMPERATURE, 'unit': '℃' }, 
        {'measurement': json[0].AIR_HUMIDITY, 'unit':'%'},
        {'measurement': json[0].AIR_PRESSURE, 'unit': 'hPa'},
        {'measurement': json[0].WIND_SPEED, 'unit': 'M/s'},
        {'measurement': json[0].MAX_WIND_GUST, 'unit': 'M/s'},
        {'measurement': json[0].WIND_DIRECTION, 'unit': ''},
        {'measurement': json[0].RAINFALL, 'unit': 'mm/u'},
        {'measurement': '-1', 'unit': 'settings'},]))
      .catch((error) => clearInterval(intervalId)) //ERROR HANDLER
      .finally(() => setLoading(false));
    },5000)
    return () => clearInterval(intervalId);
}, [ip]);

function renderItem(item) {
  if(item.unit != 'settings'){
    return (
      <TouchableOpacity  
              style={styles.block}>
              <Text style={{fontSize:40, margin:8}} adjustsFontSizeToFit numberOfLines={1} >{item.measurement} {item.unit}</Text>
      </TouchableOpacity>
    )
} else {
    return (
      <TouchableOpacity onPress = {enterMenu} style={styles.block}>
              <SimpleLineIcons name="settings" size={24} color="black" />
      </TouchableOpacity>
    )
  };
};

    return (
      <View style={{ flex: 1, paddingLeft: 8, paddingRight: 8, paddingTop: 24, backgroundColor: 'dimgray', textAlign: 'center' }}>   
          <FlatList
          numColumns={2}
            data={data}
            renderItem={({ item }) => renderItem(item)}
          />
        <Modal 
          transparent={true}
          visible={menu}
        >
          <View style={styles.modalView}>
            <Text style={{fontSize:40}} adjustsFontSizeToFit numberOfLines={1}>
              {"Settings"}
            </Text>

            <View style={styles.row}>
              <Text style={{marginRight:10, fontWeight:"bold"}}>
                Home Ip:
              </Text>
              <TextInput 
                style={{borderColor: 'gray', borderWidth: 1, borderRadius:4, padding:4}}
                placeholder="Enter Home Ip" 
                onChangeText={onChangeIp}
                value={ip}
              />
           </View>

            <TextInput
              
            />
            <Button title="exit" onPress = {()=>{setMenu(false)}}/>
          </View>
         </Modal>
      </View>
    );
};

const styles = StyleSheet.create({
  block: {
    flex:1/2,
    aspectRatio:1,
    borderColor: 'black',
    borderRadius: 16,
    borderStyle: 'dashed',
    borderWidth: 3,
    margin: 4,
    justifyContent: 'center', //Centered vertically
    alignItems: 'center', // Centered horizontally
    fontSize: 60
  },
  modalView: {
    margin: 20,
    backgroundColor: "white",
    borderRadius: 20,
    padding: 20,
    alignItems: "center",
  },
  row: {
    margin: 10,
    flexDirection: "row",
    alignItems:'center',
    justifyContent: 'space-between'
  },
});


