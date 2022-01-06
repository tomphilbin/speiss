import * as React from 'react'
import { SafeAreaView, Text, View, StatusBar, Pressable } from 'react-native'
import Geolocation, { GeolocationResponse } from '@react-native-community/geolocation'
import MapView from 'react-native-maps'
import { SwipeablePanel } from 'rn-swipeable-panel'
import SafeArea, { EventPayload as SafeAreaPayload } from 'react-native-safe-area'
import AngleUp from './assets/svg/angle-up-solid.svg'

StatusBar.setHidden(true)

const App: React.FC = () => {
  const [position, setPosition] = React.useState<GeolocationResponse>()
  const [isPanelActive, setIsPanelActive] = React.useState(false)
  const [safeAreaInsets, setSafeAreaInsets] = React.useState<SafeAreaPayload['safeAreaInsets']>()
  const [stations, setStations] = React.useState<{ name: string; id: number }[]>([])

  React.useEffect(() => {
    Geolocation.requestAuthorization()
    Geolocation.getCurrentPosition((p) => setPosition(p))
    SafeArea.getSafeAreaInsetsForRootView().then((result) => setSafeAreaInsets(result.safeAreaInsets))
  }, [])

  React.useEffect(() => {
    if (position) {
      fetch('http://localhost:5055/stations')
        .then((response) => response.json())
        .then((json) => setStations(json))
    }
  }, [position])

  return position ? (
    <View style={{ flex: 1 }}>
      <MapView
        style={{ flex: 1 }}
        initialRegion={{
          latitude: position.coords.latitude,
          longitude: position.coords.longitude,
          latitudeDelta: 0.0922,
          longitudeDelta: 0.0421,
        }}
        mapType="mutedStandard"
        userInterfaceStyle="dark"
      />
      {!isPanelActive ? (
        <View
          style={{
            position: 'absolute',
            left: 0,
            right: 0,
            bottom: safeAreaInsets?.bottom ?? 0,
            justifyContent: 'center',
            alignItems: 'center',
          }}
        >
          <Pressable
            onPress={() => setIsPanelActive(true)}
            style={{
              backgroundColor: '#fff',
              width: 66,
              height: 66,
              padding: 10,
              borderRadius: 66,
              shadowColor: '#000',
              shadowOffset: { width: 0, height: 2 },
              shadowOpacity: 0.8,
              shadowRadius: 200,
              paddingBottom: 14,
            }}
          >
            <AngleUp color="#000" />
          </Pressable>
        </View>
      ) : null}
      <SwipeablePanel fullWidth isActive={isPanelActive} closeOnTouchOutside onClose={() => setIsPanelActive(false)}>
        <View style={{ flex: 1 }}>
          {stations.map((station) => (
            <Text key={station.id} style={{ padding: 10 }}>
              {station.name}
            </Text>
          ))}
        </View>
      </SwipeablePanel>
    </View>
  ) : (
    <SafeAreaView>
      <Text>Loading...</Text>
    </SafeAreaView>
  )
}

export default App
