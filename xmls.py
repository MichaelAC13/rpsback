class setxml():
   def header(self,obj):
      self.NumeroLote = obj['NumeroLote']
      self.Cnpj = obj['Cnpj']
      self.InscricaoMunicipal = obj['InscricaoMunicipal']
      self.QuantidadeRps = obj['QuantidadeRps']
      
      header  = f'''<EnviarLoteRpsEnvio>
         <LoteRps>
            <NumeroLote>{self.NumeroLote}</NumeroLote>
            <Cnpj>{self.Cnpj}</Cnpj>
            <InscricaoMunicipal>{self.InscricaoMunicipal}</InscricaoMunicipal>
            <QuantidadeRps>{self.QuantidadeRps}</QuantidadeRps>
            <ListaRps>'''
      try:
         return (header,201)
      except Exception as e:
         return (e,400)

   def rps(self,obj):
      self.Numero = obj['Numero']
      self.Serie = obj['Serie']
      self.Tipo = obj['Tipo']
      self.DataEmissao = obj['DataEmissao']
      self.NaturezaOperacao = obj['NaturezaOperacao']
      self.RegimeEspecialTributacao = obj['RegimeEspecialTributacao']
      self.OptanteSimplesNacional = obj['OptanteSimplesNacional']
      self.IncentivadorCultural = obj['IncentivadorCultural']
      self.Status = obj['Status']
      self.ValorServicos=obj['ValorServicos']
      self.ValorDeducoes=obj['ValorDeducoes']
      self.ValorPis=obj['ValorPis']
      self.ValorCofins=obj['ValorCofins']
      self.ValorInss=obj['ValorInss']
      self.ValorIr=obj['ValorIr']
      self.ValorCsll=obj['ValorCsll']
      self.IssRetido=obj['IssRetido']
      self.ValorIss=obj['ValorIss']
      self.ValorIssRetido=obj['ValorIssRetido']
      self.OutrasRetencoes=obj['OutrasRetencoes']
      self.BaseCalculo=obj['BaseCalculo']
      self.Aliquota=obj['Aliquota']
      self.ValorLiquidoNfse=obj['ValorLiquidoNfse']
      self.DescontoIncondicionado=obj['DescontoIncondicionado']
      self.DescontoCondicionado=obj['DescontoCondicionado']
      self.ItemListaServico=obj['ItemListaServico']
      self.Discriminacao=obj['Discriminacao']
      self.CodigoMunicipio=obj['CodigoMunicipio']
      self.Cnpj=obj['Cnpj']
      self.InscricaoMunicipal=obj['InscricaoMunicipal']
      self.CpfCnpj=obj['CpfCnpj']
      self.RazaoSocial=obj['RazaoSocial']
      self.Endereco=obj['Endereco']
      self.Numero=obj['Numero']
      self.Complemento=obj['Complemento']
      self.Bairro=obj['Bairro']
      self.CodigoMunicipio=obj['CodigoMunicipio']
      self.Uf=obj['Uf']
      self.Cep=obj['Cep']
      self.Email=obj['Email']

      rps=f'''         <Rps>
                  <InfRps>
                     <IdentificacaoRps>
                        <Numero>{self.Numero}</Numero>
                        <Serie>{self.Serie}</Serie>
                        <Tipo>{self.Tipo}</Tipo>
                     </IdentificacaoRps>
                     <DataEmissao>{self.DataEmissao}</DataEmissao>
                     <NaturezaOperacao>{self.NaturezaOperacao}</NaturezaOperacao>
                     <RegimeEspecialTributacao>{self.RegimeEspecialTributacao}</RegimeEspecialTributacao>
                     <OptanteSimplesNacional>{self.OptanteSimplesNacional}</OptanteSimplesNacional>
                     <IncentivadorCultural>{self.IncentivadorCultural}</IncentivadorCultural>
                     <Status>{self.Status}</Status>
                     <Servico>
                        <Valores>
                           <ValorServicos>{self.ValorServicos}</ValorServicos>
                           <ValorDeducoes>{self.ValorDeducoes}</ValorDeducoes>
                           <ValorPis>{self.ValorPis}</ValorPis>
                           <ValorCofins>{self.ValorCofins}</ValorCofins>
                           <ValorInss>{self.ValorInss}</ValorInss>
                           <ValorIr>{self.ValorIr}</ValorIr>
                           <ValorCsll>{self.ValorCsll}</ValorCsll>
                           <IssRetido>{self.IssRetido}</IssRetido>
                           <ValorIss>{self.ValorIss}</ValorIss>
                           <ValorIssRetido>{self.ValorIssRetido}</ValorIssRetido>
                           <OutrasRetencoes>{self.OutrasRetencoes}</OutrasRetencoes>
                           <BaseCalculo>{self.BaseCalculo}</BaseCalculo>
                           <Aliquota>{self.Aliquota}</Aliquota>
                           <ValorLiquidoNfse>{self.ValorLiquidoNfse}</ValorLiquidoNfse>
                           <DescontoIncondicionado>{self.DescontoIncondicionado}</DescontoIncondicionado>
                           <DescontoCondicionado>{self.DescontoCondicionado}</DescontoCondicionado>
                        </Valores>
                        <ItemListaServico>{self.ItemListaServico}</ItemListaServico>
                        <Discriminacao>{self.Discriminacao}</Discriminacao>
                        <CodigoMunicipio>{self.CodigoMunicipio}</CodigoMunicipio>
                     </Servico>
                     <Prestador>
                        <Cnpj>{self.Cnpj}</Cnpj>
                        <InscricaoMunicipal>{self.InscricaoMunicipal}</InscricaoMunicipal>
                     </Prestador>
                     <Tomador>
                        <IdentificacaoTomador>
                           <CpfCnpj>
                              <CpfCnpj>{self.CpfCnpj}</CpfCnpj>
                           </CpfCnpj>
                        </IdentificacaoTomador>
                        <RazaoSocial>{self.RazaoSocial}</RazaoSocial>
                        <Endereco>
                           <Endereco>{self.Endereco}</Endereco>
                           <Numero>{self.Numero}</Numero>
                           <Complemento>{self.Complemento}</Complemento>
                           <Bairro>{self.Bairro}</Bairro>
                           <CodigoMunicipio>{self.CodigoMunicipio}</CodigoMunicipio>
                           <Uf>{self.Uf}</Uf>
                           <Cep>{self.Cep}</Cep>
                        </Endereco>
                        <Contato>
                           <Email>{self.Email}</Email>
                        </Contato>
                     </Tomador>
                  </InfRps>
               </Rps>'''
      try:
         return (rps,201)
      except Exception as e:
         return (e,400)

   def baseboard():
      baseboard=f'''      </ListaRps>
         </LoteRps>
         </EnviarLoteRpsEnvio>'''
      try:
         return baseboard
      except Exception as e:
         return e