import React from 'react'
import { LinearGradient } from 'expo-linear-gradient';
import { StyleSheet, View, Text } from 'react-native'
import { Entypo } from '@expo/vector-icons';
import { Feather } from '@expo/vector-icons';
import { Ionicons } from '@expo/vector-icons';

const HelloWorldApp = () => {
  return (
    <LinearGradient colors={['#2C5364', '#203A43', '#0F2027']} style={styles.linearGradient}>
      
      
      
      
      <View style={styles.header}>
        <Text>Header</Text>
      </View>

      <View  style={styles.content}> 
        

        <View style={styles.Temperature}>
          <Text style={{ fontSize: 120 ,  marginLeft:40, color: '#FAF9F6'}}> 1° </Text>
        </View>


        <View  style={styles.miniInfo}>
          <Entypo name="location-pin" size={24} color="white" />
          <Text style={{color: '#FAF9F6'}}>Thuis</Text>
        </View>

      </View>


      <View style={styles.footer}>
        <View style={styles.miniInfo}>
          <Ionicons name="rainy" size={24} color="white" style={styles.miniIcon} />
          <Text style={{color: '#FAF9F6'}}>0,0 mm/u</Text>
        </View>
        <View style={styles.miniInfo}>
          <Entypo name="compass" size={24} color="white" style={styles.miniIcon} />
          <Text style={{color: '#FAF9F6'}}>NNW</Text>
        </View>
        <View style={styles.miniInfo}>
         <Feather name="wind" size={24} color="white" style={styles.miniIcon} />
         <Text style={{color: '#FAF9F6'}}>15 m/s</Text>
        </View>
      </View>


    </LinearGradient>
  );
};
export default HelloWorldApp;


var styles = StyleSheet.create({
  linearGradient: {
    justifyContent: 'space-between',
    flexDirection: 'column',
    flex: 1,
    paddingLeft: 15,
    paddingRight: 15,
    includeFontPadding: false,
  },
  footer: {
    paddingBottom: 150,
    flexDirection: 'row',
    justifyContent: 'space-around'
  },
  Temperature: {
    flexDirection: 'row',
    justifyContent: 'space-around',
  },
  TemperatureAddons: {
    width: 80,
    flexDirection: 'column',
    justifyContent: 'center',
    marginRight:40,
    marginBottom: 5,
  },
  content: {
    justifyContent: 'center',
    flexDirection: 'column',
    marginBottom: 120
  },
  miniInfo: {
    justifyContent: 'center',
    flexDirection: 'row',
    alignItems: 'center'
  },
  miniIcon: {
    paddingHorizontal: 10,
  }
});
