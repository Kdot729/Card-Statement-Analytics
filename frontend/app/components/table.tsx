import {View, Text, StyleSheet, FlatList} from 'react-native';
import { useFetch } from '../../scripts/fetch';
import { Use_Context, Create_Context } from '../../scripts/hook/context';
import React from "react";
import { Center } from '../css/main';
import Arrow from './arrow';

const Table_Row = ({Component}: {Component: JSX.Element}): JSX.Element =>
{
    const Row_Styles = [Table_Styles["Row"], Center, Margin(2)]
    
    return <View style={Row_Styles}>{Component}</View>
}

export const Table = () =>
{
    const PDF_ID = Use_Context(Create_Context)
    const {Activity_Period, Statistic} = useFetch(PDF_ID)

    const Header = Object.keys(Statistic ? Statistic[0] : {})
    const Date_Header_Font_Size = 20

    const Table_Header =    <View style={Table_Element("rgb(190, 189, 189)")}>                 
                            {
                                Header.map((Header: string) =>
                                {
                                    const Table_Header_Font_Size = Date_Header_Font_Size - 3
                                    const Text_Styles = [Table_Styles["Header_Cell"], Font_Size(Table_Header_Font_Size)]
                                    
                                    const Component =   <>
                                                            <Text style={Text_Styles}>{Header}</Text>
                                                            <Arrow />
                                                        </>

                                    return <Table_Row key={Header} Component={Component} />
                                })
                            }
                            </View>

    const Statistics = ({item}) => 
                        {
                            const Row = Object.entries(item).map(([Category, Value]) =>
                                {
                                    const Row_Font_Size = Date_Header_Font_Size - 6
                                    
                                    return <Table_Row key={Category}
                                        Component={<Text style={Font_Size(Row_Font_Size)}>{Value}</Text>} />
                                })

                            const Row_Container_Styles = [Table_Styles["Body"], Table_Element("rgb(228, 228, 228)")]

                            return <View style={Row_Container_Styles} key={item["ID"]}>{Row}</View>
                        }

    const Container_Styles = [Table_Styles["Container"], Center]
    const Header_Styles = [Font_Size(Date_Header_Font_Size), Margin(3)]

    return  Statistic && Activity_Period ? 
            <View style={Container_Styles}>
                <Text style={Header_Styles}>{Activity_Period}</Text>
                <View style={Margin(3)}>
                <FlatList data={Statistic} ListHeaderComponent={Table_Header} 
                keyExtractor={(Transaction) => Transaction["ID"]} renderItem={Statistics} />
                </View>
            </View> : 
            null
}

const Table_Styles = StyleSheet.create(
{
    Container: {flex: 1},
    Header_Cell: {color: "rgb(11, 79, 180)", fontWeight: "bold"},
    Body: {padding: 5},
    Row: {width: "15%", flexDirection: "row"}
})

const Table_Element = (Background_Color) =>
{
    return StyleSheet.create({Element: {flexDirection: "row", backgroundColor: Background_Color}})["Element"]
}

const Font_Size = (Size: number) =>
{
    return StyleSheet.create({Font_Size: {fontSize: Size}})["Font_Size"]
}

const Margin = (Margin: number) =>
{
    return StyleSheet.create({Margin: {margin: Margin}})["Margin"]
}