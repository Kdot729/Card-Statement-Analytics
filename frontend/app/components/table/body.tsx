import { View, Text, StyleSheet } from 'react-native'
import React from 'react'
import { Font_Size } from '@/scripts/css/main'
import { Table_Element } from '@/scripts/css/table'
import Table_Row from './row'

const Table_Body = ({item}) => 
{
    const Row = Object.entries(item).map(([Category, Value]) =>
    {
        return <Table_Row key={Category}
            Component={<Text style={Font_Size(14)}>{Value}</Text>} />
    })

    const Row_Container_Styles = [Body_Styles, Table_Element("rgb(228, 228, 228)")]

    return <View style={Row_Container_Styles} key={item["ID"]}>{Row}</View>
}

const Body_Styles = StyleSheet.create(
{
    Body: {padding: 5},
})["Body"]

export default Table_Body