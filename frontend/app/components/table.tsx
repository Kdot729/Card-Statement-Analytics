import {View, Text, StyleSheet, FlatList} from 'react-native';
import { useFetch } from '../../scripts/fetch';
import { Use_Context, Create_Context } from '../../scripts/hook/context';
import React from "react";

const Table_Row = ({Text_Component}: {Text_Component: JSX.Element}): JSX.Element =>
{
    return <View style={Table_Styles["Row"]}>{Text_Component}</View>
}

export const Table = () =>
{
    const PDF_ID = Use_Context(Create_Context)
    const {Activity_Period, Statistic} = useFetch(PDF_ID)

    const Header = Object.keys(Statistic ? Statistic[0] : {})

    const Table_Header =    <View style={Table_Styles["Header"]}>                 
                            {
                                Header.map((Header: string) =>
                                {
                                    return <Table_Row key={Header} 
                                        Text_Component={<Text style={Table_Styles["Header_Cell"]}>{Header}</Text>} />
                                })
                            }
                            </View>

    const Statistics = ({item}) => 
                        {
                            const Row = Object.entries(item).map(([Category, Value]) =>
                                {
                                    return <Table_Row key={Category}
                                        Text_Component={<Text style={Table_Styles["Body_Cell"]}>{Value}</Text>} />
                                })

                            return <View style={Table_Styles["Body"]} key={item["ID"]}>{Row}</View>
                        }

    
    return  Statistic && Activity_Period ? 
            <View style={Table_Styles["Container"]}>
                <Text>{Activity_Period}</Text>
                <View style={Table_Styles["Table"]}>
                <FlatList data={Statistic} ListHeaderComponent={Table_Header} 
                keyExtractor={(Transaction) => Transaction["ID"]} renderItem={Statistics} />
                </View>
            </View> : 
            null
}

const Table_Styles = StyleSheet.create(
{
    Container: {justifyContent: "center", alignItems: "center", flex: 1},
    Table: {margin: 3},
    Header: {flexDirection: "row", backgroundColor: "rgb(190, 189, 189)"},
    Header_Cell: {color: "rgb(11, 79, 180)", fontWeight: "bold", fontSize: 15},
    Body: {flexDirection: "row", padding: 5, backgroundColor: "rgb(228, 228, 228)"},
    Body_Cell: {fontSize: 11},
    Row: {width: "15%", justifyContent: "center", alignItems: "center", margin: 2}
})