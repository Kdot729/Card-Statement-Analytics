import Svg, { Path } from "react-native-svg"
import {View, Text, Button, StyleSheet} from 'react-native';
import { useState, useContext } from 'react';
import * as DocumentPicker from 'expo-document-picker';
import { AxiosInstance } from "../../scripts/axios_interceptor";
import { Table } from "./table";
import { Create_Context } from "../../scripts/hook/context";

const Upload = (properties) =>
{
    return  <Svg xmlns="http://www.w3.org/2000/svg" width={384} height={384} viewBox="0 0 24 24" {...properties}>
                <Path
                fill="#369af2"
                d="M15 4H5v16h14V8h-4zM3 2.992C3 2.444 3.447 2 3.999 2H16l5 5v13.993A1 1 0 0 1 20.007 22H3.993A1 1 0 0 1 3 21.008zM13 12v4h-2v-4H8l4-4 4 4z"/>
            </Svg>
}

export const File = () =>
{
    const [PDF_ID, Set_PDF_ID] = useState("")

    const Upload_File = async () => 
    {
        const PDF_Document = await DocumentPicker.getDocumentAsync({type: 'application/pdf'})

        const PDF = PDF_Document.assets[0].uri
        const No_Header_PDF = PDF.split(",")[1]
        const PDF_Last_Characters = No_Header_PDF.substr(No_Header_PDF.length - 16);
        const ID = PDF_Last_Characters.slice(0,-1)

        Set_PDF_ID(ID)
        await AxiosInstance.post("post/PDF", {PDF_ID: ID, PDF})

    }

    return  PDF_ID ? 
            <Create_Context.Provider value={PDF_ID}>
                <Table />
            </Create_Context.Provider > : 
            <View>
                <Text style={Styles.Header}>Upload PDF</Text>
                <Upload />
                <Button title="Select Document" onPress={Upload_File}/>
            </View>
}

const Styles = StyleSheet.create(
{
    Header:    {
                    color: 'black',
                    fontSize: 28,
                    textAlign: 'center',
                    marginVertical: 40,
                }

})

export default File