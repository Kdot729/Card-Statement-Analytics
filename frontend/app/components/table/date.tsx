import { Text } from 'react-native'
import React from 'react'
import { useFetch } from '@/scripts/fetch'
import { Use_Context, Create_Context } from '@/scripts/hook/context'
import { Font_Size, Margin } from '@/scripts/css/main'

const Table_Date = () => 
{
    const PDF_ID = Use_Context(Create_Context)
    const {Activity_Period} = useFetch("get/PDF", PDF_ID)
    
    const Header_Styles = [Font_Size(20), Margin(3)]

    return <Text style={Header_Styles}>{Activity_Period}</Text>
}

export default Table_Date