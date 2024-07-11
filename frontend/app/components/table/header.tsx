import { View, Text, StyleSheet } from 'react-native'
import React from 'react'
import { useFetch } from '@/scripts/fetch'
import { Use_Context, Create_Context } from '@/scripts/hook/context'
import Arrow from '../arrow'
import { Table_Element } from '@/scripts/css/table'
import { Font_Size } from '@/scripts/css/main'
import Table_Row from './row'

const Table_Header = () => 
{
    const PDF_ID = Use_Context(Create_Context)
    const {Activity_Period, Statistic} = useFetch("get/PDF", PDF_ID)
    
    const Columns = Object.keys(Statistic ? Statistic[0] : {})

    const Header = Columns.map((Column: string) =>
                    {
                        const Text_Styles = [Header_Styles, Font_Size(17)]
                        
                        const Component =   <>
                                                <Text style={Text_Styles}>{Column}</Text>
                                                <Arrow Column={Column}/>
                                            </>

                        return <Table_Row key={Column} Component={Component} />
                    })
                            

    return Statistic && Activity_Period ? <View style={Table_Element("rgb(190, 189, 189)")}>{Header}</View> : null
}

const Header_Styles = StyleSheet.create(
{
    Header: {color: "rgb(11, 79, 180)", fontWeight: "bold"}
})["Header"]

export default Table_Header