
import { Center, Margin } from '@/scripts/css/main';
import {View, StyleSheet} from 'react-native';

const Table_Row = ({Component}: {Component: JSX.Element}): JSX.Element =>
{
    const Row_Styles = [Row_CSS, Center, Margin(2)]
    
    return <View style={Row_Styles}>{Component}</View>
}

const Row_CSS = StyleSheet.create(
{
    Row: {width: "15%", flexDirection: "row"}
})["Row"]

export default Table_Row